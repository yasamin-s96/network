
const Container = ({ children }) => {
    return (
        <div className="h-screen bg-img bg-cover bg-center bg-no-repeat">
            <div className="container mx-auto">
                {children}
            </div>
        </div>
    )
}

export default Container