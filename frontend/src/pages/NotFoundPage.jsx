import Container from "../components/shared/Container"
import { useRouteError } from 'react-router-dom'
import { Helmet } from 'react-helmet'

const NotFoundPage = () => {

    const error = useRouteError()

    return (
        <>
            <Helmet>
                <title>
                    Page Not Found
                </title>
            </Helmet>
            <Container additionalClasses="flex flex-col justify-center items-center text-yellow-50 space-y-5">
                <h1 className="text-6xl font-semibold">Oops!</h1>
                <p className="text-xl">Sorry, an unexpected error has occured.</p>
                <p>
                    <i>{error.statusText || error.message}</i>
                </p>
            </Container>
        </>

    )
}

export default NotFoundPage