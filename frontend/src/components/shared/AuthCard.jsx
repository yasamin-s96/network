
const AuthCard = ({ children }) => {
    return (
        <div className="bg-slate-50 p-3 w-full lg:w-1/2 text-center flex items-center justify-center">
            <div className="w-96 p-5 bg-white rounded-lg shadow-md border border-stone-200">
                {children}
            </div>
        </div>
    )
}

export default AuthCard